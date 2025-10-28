import matplotlib.pyplot as plt

def get_sales_data():
    """Get sales data from user for all categories"""
    
    print("VisProg Inc. - Sales Data Entry")
    print("=" * 50)
    
    # Get sales data for Laptops and Computers
    print("\nLaptops and Computers:")
    laptops_q1 = float(input("Enter sales for Q1 (Jan-Mar):₱ "))
    laptops_q2 = float(input("Enter sales for Q2 (Apr-Jun):₱ "))
    laptops_q3 = float(input("Enter sales for Q3 (Jul-Sep):₱ "))
    laptops_sales = [laptops_q1, laptops_q2, laptops_q3]
    
    # Get sales data for Smartphones and Tablets
    print("\nSmartphones and Tablets:")
    smartphones_q1 = float(input("Enter sales for Q1 (Jan-Mar):₱ "))
    smartphones_q2 = float(input("Enter sales for Q2 (Apr-Jun):₱ "))
    smartphones_q3 = float(input("Enter sales for Q3 (Jul-Sep):₱ "))
    smartphones_sales = [smartphones_q1, smartphones_q2, smartphones_q3]
    
    # Get sales data for Gaming Products
    print("\nGaming Products:")
    gaming_q1 = float(input("Enter sales for Q1 (Jan-Mar):₱ "))
    gaming_q2 = float(input("Enter sales for Q2 (Apr-Jun):₱ "))
    gaming_q3 = float(input("Enter sales for Q3 (Jul-Sep):₱ "))
    gaming_sales = [gaming_q1, gaming_q2, gaming_q3]
    
    # Get sales data for Computer Accessories
    print("\nComputer Accessories:")
    accessories_q1 = float(input("Enter sales for Q1 (Jan-Mar):₱ "))
    accessories_q2 = float(input("Enter sales for Q2 (Apr-Jun):₱ "))
    accessories_q3 = float(input("Enter sales for Q3 (Jul-Sep):₱ "))
    accessories_sales = [accessories_q1, accessories_q2, accessories_q3]
    
    return laptops_sales, smartphones_sales, gaming_sales, accessories_sales

def display_summary(laptops_sales, smartphones_sales, gaming_sales, accessories_sales):
    """Display sales summary"""
    
    total_laptops = sum(laptops_sales)
    total_smartphones = sum(smartphones_sales)
    total_gaming = sum(gaming_sales)
    total_accessories = sum(accessories_sales)
    
    print("\n" + "=" * 50)
    print("SALES SUMMARY")
    print("=" * 50)
    print(f"Laptops and Computers: ${total_laptops}")
    print(f"Smartphones and Tablets: ${total_smartphones}")
    print(f"Gaming Products: ${total_gaming}")
    print(f"Computer Accessories: ${total_accessories}")
    print("=" * 50)
    
    return total_laptops, total_smartphones, total_gaming, total_accessories

def create_bar_chart(laptops_sales, smartphones_sales, gaming_sales, accessories_sales):
    """Create bar chart for quarterly sales comparison"""
    
    quarters = ['Q1', 'Q2', 'Q3']
    x = [0, 1, 2]
    width = 0.2
    
    plt.figure(figsize=(10, 6))
    
    plt.bar([i - 1.5*width for i in x], laptops_sales, width, label='Laptops and Computers')
    plt.bar([i - 0.5*width for i in x], smartphones_sales, width, label='Smartphones and Tablets')
    plt.bar([i + 0.5*width for i in x], gaming_sales, width, label='Gaming Products')
    plt.bar([i + 1.5*width for i in x], accessories_sales, width, label='Computer Accessories')
    
    plt.xlabel('Quarter')
    plt.ylabel('Sales ($)')
    plt.title('VisProg Inc. - Quarterly Sales Comparison')
    plt.xticks(x, quarters)
    plt.legend()
    plt.grid(axis='y')
    
    plt.tight_layout()
    plt.show()

def create_pie_chart(total_laptops, total_smartphones, total_gaming, total_accessories):
    """Create pie chart for category distribution"""
    
    categories = ['Laptops and Computers', 'Smartphones and Tablets', 
                  'Gaming Products', 'Computer Accessories']
    total_sales = [total_laptops, total_smartphones, total_gaming, total_accessories]
    colors = ['red', 'blue', 'green', 'orange']
    
    plt.figure(figsize=(8, 8))
    
    plt.pie(total_sales, labels=categories, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('VisProg Inc. - Product Category Distribution')
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the program"""
    
    # Get sales data from user
    laptops_sales, smartphones_sales, gaming_sales, accessories_sales = get_sales_data()
    
    # Display summary
    total_laptops, total_smartphones, total_gaming, total_accessories = display_summary(
        laptops_sales, smartphones_sales, gaming_sales, accessories_sales)
    
    # Create bar chart
    create_bar_chart(laptops_sales, smartphones_sales, gaming_sales, accessories_sales)
    
    # Create pie chart
    create_pie_chart(total_laptops, total_smartphones, total_gaming, total_accessories)
    
    print("\nVisualization complete!")

# Run the program
main()