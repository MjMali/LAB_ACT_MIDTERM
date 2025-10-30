import matplotlib.pyplot as plt

# ==================== DATA INPUT FUNCTIONS ====================

def get_data_points():
    """Get data labels and values from user"""
    labels = []
    values = []
    
    while True:
        try:
            num_points = int(input("How many data points? "))
            break
        except ValueError:
            print("Error! Please enter a valid number.")
    
    for i in range(num_points):
        label = input(f"Enter label {i+1}: ")
        
        while True:
            try:
                value = float(input(f"Enter value {i+1}: "))
                break
            except ValueError:
                print("Error! Please enter a valid number.")
        
        labels.append(label)
        values.append(value)
    
    return labels, values


def get_bar_data():
    """Get data for bar graph (max 6 bars)"""
    labels = []
    values = []
    
    while True:
        try:
            num_bars = int(input("How many bars (max 6)? "))
            break
        except ValueError:
            print("Error! Please enter a valid number.")
    
    if num_bars > 6:
        print("Maximum 6 bars allowed. Setting to 6.")
        num_bars = 6
    
    for i in range(num_bars):
        label = input(f"Enter label for bar {i+1}: ")
        
        while True:
            try:
                value = float(input(f"Enter value for bar {i+1}: "))
                break
            except ValueError:
                print("Error! Please enter a valid number.")
        
        labels.append(label)
        values.append(value)
    
    return labels, values


# ==================== LINE PLOT FUNCTIONS ====================

def get_line_marker():
    """Get marker type for line plot"""
    print("\nMarker Options:")
    print("1. Circle")
    print("2. Square")
    print("3. Star")
    
    choice = input("Choose marker (1-3): ")
    
    if choice == '1':
        marker = 'o'
    elif choice == '2':
        marker = 's'
    elif choice == '3':
        marker = '*'
    else:
        marker = 'o'
    
    return marker


def get_line_color():
    """Get color for line plot"""
    print("\nColor Options:")
    print("1. Red")
    print("2. Blue")
    print("3. Yellow")
    
    choice = input("Choose color (1-3): ")
    
    if choice == '1':
        color = 'red'
    elif choice == '2':
        color = 'blue'
    elif choice == '3':
        color = 'yellow'
    else:
        color = 'red'
    
    return color


def get_line_style():
    """Get line style for line plot"""
    print("\nLine Style Options:")
    print("1. Solid")
    print("2. Dotted")
    print("3. Dashed")
    print("4. Dashed-Dotted")
    
    choice = input("Choose line style (1-4): ")
    
    if choice == '1':
        style = '-'
    elif choice == '2':
        style = ':'
    elif choice == '3':
        style = '--'
    elif choice == '4':
        style = '-.'
    else:
        style = '-'
    
    return style


def create_line_plot(labels, values, marker, color, linestyle):
    """Create and display line plot"""
    plt.figure(figsize=(10, 6))
    plt.plot(labels, values, marker=marker, color=color, linestyle=linestyle, 
             linewidth=2, markersize=15, markerfacecolor=color, 
             markeredgecolor='black', markeredgewidth=2, alpha=0.7)
    plt.xlabel('Labels')
    plt.ylabel('Values')
    plt.title('Line Plot')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# ==================== BAR GRAPH FUNCTIONS ====================

def get_bar_width():
    """Get bar width"""
    while True:
        try:
            width = float(input("Enter bar width (0.1 to 1.0, recommended 0.5): "))
            break
        except ValueError:
            print("Error! Please enter a valid number.")
    
    if width < 0.1:
        width = 0.1
    elif width > 1.0:
        width = 1.0
    
    return width


def get_bar_colors(num_bars):
    """Get colors for each bar"""
    print("\nColor Options:")
    print("1. Red")
    print("2. Blue")
    print("3. Yellow")
    print("4. Green")
    print("5. Purple")
    print("6. Orange")
    print("7. Pink")
    
    colors = []
    for i in range(num_bars):
        choice = input(f"Choose color for bar {i+1} (1-7): ")
        
        if choice == '1':
            color = 'red'
        elif choice == '2':
            color = 'blue'
        elif choice == '3':
            color = 'yellow'
        elif choice == '4':
            color = 'green'
        elif choice == '5':
            color = 'purple'
        elif choice == '6':
            color = 'orange'
        elif choice == '7':
            color = 'pink'
        else:
            color = 'blue'
        
        colors.append(color)
    
    return colors


def create_bar_graph(labels, values, width, colors):
    """Create and display bar graph"""
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, width=width, color=colors, edgecolor='black')
    plt.xlabel('Labels')
    plt.ylabel('Values')
    plt.title('Bar Graph')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()


# ==================== PIE CHART FUNCTIONS ====================

def get_explode_values(num_slices):
    """Get explode values for pie chart"""
    explode_choice = input("\nDo you want to explode any slice? (yes/no): ").lower()
    
    explode = []
    for i in range(num_slices):
        explode.append(0)
    
    if explode_choice == 'yes':
        while True:
            try:
                slice_num = int(input(f"Which slice to explode? (1-{num_slices}): "))
                if slice_num >= 1 and slice_num <= num_slices:
                    explode[slice_num - 1] = 0.1
                    break
                else:
                    print(f"Error! Please enter a number between 1 and {num_slices}.")
            except ValueError:
                print("Error! Please enter a valid number.")
    
    return explode


def get_pie_colors(num_slices):
    """Get colors for pie chart slices"""
    print("\nColor Options:")
    print("1. Red")
    print("2. Blue")
    print("3. Yellow")
    print("4. Green")
    print("5. Purple")
    print("6. Orange")
    print("7. Pink")
    
    colors = []
    for i in range(num_slices):
        choice = input(f"Choose color for slice {i+1} (1-7): ")
        
        if choice == '1':
            color = 'red'
        elif choice == '2':
            color = 'blue'
        elif choice == '3':
            color = 'yellow'
        elif choice == '4':
            color = 'green'
        elif choice == '5':
            color = 'purple'
        elif choice == '6':
            color = 'orange'
        elif choice == '7':
            color = 'pink'
        else:
            color = 'blue'
        
        colors.append(color)
    
    return colors


def get_hatch_pattern():
    """Get hatch pattern for pie chart"""
    print("\nHatch Pattern Options:")
    print("1. / (forward slash)")
    print("2. \\ (backslash)")
    print("3. | (vertical)")
    print("4. - (horizontal)")
    print("5. + (cross)")
    print("6. None")
    
    choice = input("Choose hatch pattern (1-6): ")
    
    if choice == '1':
        pattern = '/'
    elif choice == '2':
        pattern = '\\'
    elif choice == '3':
        pattern = '|'
    elif choice == '4':
        pattern = '-'
    elif choice == '5':
        pattern = '+'
    elif choice == '6':
        pattern = ''
    else:
        pattern = ''
    
    return pattern


def create_pie_chart(labels, values, explode, colors, hatch):
    """Create and display pie chart"""
    plt.figure(figsize=(10, 8))
    
    wedges, texts, autotexts = plt.pie(
        values, 
        labels=labels, 
        explode=explode,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True
    )
    
    # Apply hatch pattern to all wedges if selected
    if hatch != '':
        for wedge in wedges:
            wedge.set_hatch(hatch)
            wedge.set_alpha(0.7)
            wedge.set_edgecolor('black')
            wedge.set_linewidth(2)
    
    plt.title('Pie Chart')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


# ==================== MAIN MENU FUNCTIONS ====================

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("DATA VISUALIZATION PROGRAM")
    print("="*50)
    print("1. Line Plot")
    print("2. Bar Graph")
    print("3. Pie Chart")
    print("4. Exit")
    print("="*50)


def handle_line_plot():
    """Handle line plot creation"""
    print("\n--- LINE PLOT ---")
    labels, values = get_data_points()
    marker = get_line_marker()
    color = get_line_color()
    linestyle = get_line_style()
    create_line_plot(labels, values, marker, color, linestyle)


def handle_bar_graph():
    """Handle bar graph creation"""
    print("\n--- BAR GRAPH ---")
    labels, values = get_bar_data()
    width = get_bar_width()
    colors = get_bar_colors(len(labels))
    create_bar_graph(labels, values, width, colors)


def handle_pie_chart():
    """Handle pie chart creation"""
    print("\n--- PIE CHART ---")
    labels, values = get_data_points()
    
    if len(values) < 5:
        print("Note: Pie chart works best with at least 5 values.")
    
    explode = get_explode_values(len(values))
    colors = get_pie_colors(len(values))
    hatch = get_hatch_pattern()
    create_pie_chart(labels, values, explode, colors, hatch)


def main():
    """Main program function"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            handle_line_plot()
        
        elif choice == '2':
            handle_bar_graph()
        
        elif choice == '3':
            handle_pie_chart()
        
        elif choice == '4':
            print("\nThank you for using the Data Visualization Program!")
            break
        
        else:
            print("\nInvalid choice! Please enter 1-4.")


# ==================== PROGRAM ENTRY POINT ====================

if __name__ == "__main__":
    main()