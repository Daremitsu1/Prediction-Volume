# 1. Import dependencies
library(dplyr)

# 2. Read in the data
sales_data <- read.csv("C:/Users/aviparna.biswas/Python Projects/New folder/sales_data.csv")

# 3. Use dplyr to get a summary of the data
sales_summary <- sales_data %>% 
  group_by(Product_Category, Sub_Category, Product) %>% 
  summarize(mean_quantity = mean(Order_Quantity),
            mean_unit_price = mean(Unit_Price),
            mean_unit_cost = mean(Unit_Cost),
            mean_profit = mean(Profit))

# 4. Print the summary data
print(sales_summary)

# Use dplyr to look at average customer age by gender
avg_age_by_gender <- sales_data %>% 
  group_by(Customer_Gender) %>% 
  summarize(mean_age = mean(Customer_Age))

# Print the result
print(avg_age_by_gender)

# Use dplyr to find the top 5 states with the most revenue
top_states_by_revenue <- sales_data %>% 
  group_by(State) %>% 
  summarize(total_revenue = sum(Revenue)) %>% 
  arrange(desc(total_revenue)) %>% 
  head(5)

# Print the result
print(top_states_by_revenue)
