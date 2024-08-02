import matplotlib.pyplot as plt

# Create a simple plot
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])

# Specify the file path for saving the figure on your desktop
file_path = "C:\Users\Tushar srivastava\OneDrive\Desktop\Front Pages.jpg"

# Save the figure in JPG format
plt.savefig("C:\Users\Tushar srivastava\OneDrive\Desktop\Front Pages.jpg")

# Close the plot if you want
plt.close()

print("Figure saved as {C:\Users\Tushar srivastava\OneDrive\Desktop\Front Pages}")
