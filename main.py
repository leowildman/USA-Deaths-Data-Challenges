import matplotlib_stuff

def pretty_print(data:any):
    """Pretty prints data, 
    checks whether data is iterable and prints in a nice format

    Args:
        data (Any): data to be printed
    """
    if type(data) == dict:
        for item in data:
            print(str(item)+":")
            pretty_print(data[item])
            print("\n")
    elif type(data) in [list, tuple]:
        for item in data: print(item)
    else:
        print(data) 
       
class death:
  """
    Class of each individual death statistic.
    Takes in all categories listed within csv and type checks them.
  """
  def __init__(self, year:int, cause, state, number_of_deaths:int, death_rate:int):
    self.year = int(year)
    self.cause = cause
    self.state = state
    self.number_of_deaths = int(number_of_deaths)
    self.death_rate = float(death_rate)
  def __repr__(self):
    return f"Year: {self.year}, Cause: {self.cause}, State: {self.state}, Number of deaths: {self.number_of_deaths}, death_rate: {self.death_rate}"

# file handling

class challenges:
    def __init__(self, data_filename="", data=[]) -> None:
        """Challenges container and file opener.
        Leave either argument empty to specify if a file needs to be read or not.

        Args:
            data_filename (str, optional): filename of data to be read. Defaults to "".
            data (list, optional): pre-read data. Defaults to [].
        """
        self.data = data
        
        if self.data == []:
            with open(data_filename, "r") as injuries_file:
                text = injuries_file.readlines()[1:]
                for line in text:
                    splitted = line.split(",")
                    self.data.append(death(splitted[0], splitted[1], splitted[2], splitted[3], splitted[4]))
      
    def two(self):
        states = []
        for item in self.data:
            if item.state not in states:
                states.append(item.state)
        return states

    def three(self):
        death_num = []
        for item in self.data:
            if item.cause == "Alzheimer's disease" and item.year == 2012:
                death_num.append(item.number_of_deaths)
        return death_num

    def four(self):
        cases = []
        for item in self.data:
            if item.cause == "Alzheimer's disease" and item.year == 2012:
                cases.append([item.number_of_deaths, item.death_rate])
        return cases

    def five(self):
        cases = []
        for item in self.data:
            if item.cause == "Alzheimer's disease" and item.year == 2012:
                cases.append([item.number_of_deaths, item.death_rate, item.state])
        return cases

    def six(self, state="Nebraska") -> tuple:
        """Challenge six - returns most common cause of death

        Args:
            state (str, optional): State in question. Defaults to "Nebraska".

        Returns:
            tuple: Tuple in format (cause, total deaths)
        """
        filtered_data = []
        categorised_data = {}
        
        #Filters to only Nebraska
        for item in self.data:
            if item.state == state:
                filtered_data.append(item)

        #Categorises into causes
        for item in filtered_data:
            if item.cause not in categorised_data.keys():
                categorised_data[item.cause] = 0
            categorised_data[item.cause] += item.number_of_deaths

        categorised_data["All causes"] = 0
        
        top = ("", 0)
        for key in categorised_data:
            if categorised_data[key] > top[1]:
                top = (key, categorised_data[key])
        return top
        
    def seven(self, state="New Jersey") -> dict:
        """Challenge seven.

        Args:
            state (str, optional): State in Question. Defaults to "New Jersey".

        Returns:
            dict: ALl years with their respective death totals from the top ten causes of death.
        """
        filtered_data = []
        categorised_data = {}
        
        for item in self.data:
            if item.state == state:
                filtered_data.append(item)
                
        for item in filtered_data:
            if item.year not in categorised_data.keys():
                categorised_data[item.year] = []
            categorised_data[item.year].append(item)
            
        final_data = {}    
        
        for year in categorised_data:
            deaths_categorised_data = {}
            for item in categorised_data[year]:
                if item.cause != "All causes":
                    if item.number_of_deaths not in deaths_categorised_data.keys():
                        deaths_categorised_data[item.number_of_deaths] = []
                        
                    deaths_categorised_data[item.number_of_deaths].append(item)
            
            top_ten_keys = (sorted(deaths_categorised_data.keys(), reverse=True)[:10])
            top_ten = {}
            for key in top_ten_keys:
                top_ten[key] = deaths_categorised_data[key]
            
            total_deaths = 0
            for item in top_ten:
                for i in top_ten[item]:
                    total_deaths += i.number_of_deaths
            final_data[year] = total_deaths
        return final_data
        
    def eight(self) -> None:
        """
        Plots a graph of deaths per state over time.
        """
        states = self.two()
        big_tracking_data = {}
        
        for state in states:
            big_tracking_data[state] = self.seven(state=state)
            
        big_tracking_data.pop("United States")
        
        matplotlib_stuff.plot(big_tracking_data)
                

c = challenges(data_filename="injuries.csv")

print("Challenge Two:")
pretty_print(c.two())
input("continue...?")
print("Challenge Three:")
pretty_print(c.three())
input("continue...?")
print("Challenge Four:")
pretty_print(c.four())
input("continue...?")
print("Challenge Five:")
pretty_print(c.five())
input("continue...?")
print("Challenge Six:")
pretty_print(c.six())
input("continue...?")
print("Challenge Seven:")
pretty_print(c.seven())
input("continue...?")
print("Challenge Eight:")
pretty_print(c.eight())