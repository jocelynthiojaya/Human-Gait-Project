from matplotlib import pyplot as plt

def outputGraph(filename, folder, nametag,
                x1, y1, title1,
                x2, y2, title2,
                x3, y3, title3,
                x4, y4, title4,
                x5, y5, title5):
    fig, axs = plt.subplots(3, 2)
    fig.tight_layout()
    fig.delaxes(axs[2][1])

    axs[0, 0].plot(x1, y1)
    axs[0, 0].set_title(title1)
    axs[0, 1].plot(x2, y2, 'tab:orange')
    axs[0, 1].set_title(title2)
    axs[1, 0].plot(x3, y3, 'tab:green')
    axs[1, 0].set_title(title3)
    axs[1, 1].plot(x4, y4, 'tab:red')
    axs[1, 1].set_title(title4)
    axs[2, 0].plot(x5, y5, 'tab:purple')
    axs[2, 0].set_title(title5)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    plt.savefig(folder +"/" + nametag + "_graphoutput/" + filename + '.png')
