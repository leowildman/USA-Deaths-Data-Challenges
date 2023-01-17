import matplotlib.pyplot as plt

def plot(big_tracking_data):
    fig, ax = plt.subplots()
    
    fig.suptitle("Number of Deaths per year per state. Click state line to toggle visibility.")
    ax.set_xlabel("Year")
    ax.set_ylabel("Deaths")
    lines = []
    for state in big_tracking_data:
        line, = ax.plot(big_tracking_data[state].keys(), big_tracking_data[state].values(), label=state)
        ax.locator_params(nbins=25, axis='x')
        lines.append(line)
    
    leg = ax.legend(fancybox=True, shadow=True, bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize="xx-small")
    lined = {}
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(True)
        lined[legline] = origline
        origline.set_visible(False)
        
    def on_pick(event):
        # On the pick event, find the original line corresponding to the legend
        # proxy line, and toggle its visibility.
        legline = event.artist
        origline = lined[legline]
        visible = not origline.get_visible()
        origline.set_visible(visible)
        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled.
        legline.set_alpha(1.0 if visible else 0.2)
        fig.canvas.draw()
    
    fig.canvas.mpl_connect('pick_event', on_pick)
    plt.show()