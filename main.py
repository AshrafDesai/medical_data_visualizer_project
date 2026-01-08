from medical_data_visualizer import draw_cat_plot, draw_heat_map

def main():
    # Draw Categorical Plot
    cat_fig = draw_cat_plot()
    cat_fig.savefig("catplot.png")
    print("Categorical plot saved as catplot.png")

    # Draw Heat Map
    heat_fig = draw_heat_map()
    heat_fig.savefig("heatmap.png")
    print("Heatmap saved as heatmap.png")

if __name__ == "__main__":
    main()
