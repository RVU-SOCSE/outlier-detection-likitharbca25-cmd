Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("C:/Users/Chandu/Downloads/10prog_4laptops.csv")
plt.boxplot(df2["Screen_size_inches"],notch = True, vert = False,showmeans =
True, sym = "*", patch_artist=True, widths= 0.1 ) # medianprops = median_shape,
flierprops = red_circle , meanprops = mean_shape , sym = "x" , "+"," *"
SyntaxError: multiple statements found while compiling a single statement
plt.boxplot(df2["Screen_size_inches"],notch = True, vert = False,showmeans = True, sym ="*", patch_artist=True, widths= 0.1 )
{'whiskers': [<matplotlib.lines.Line2D object at 0x000001D113EBF890>, <matplotlib.lines.Line2D object at 0x000001D113F55310>], 'caps': [<matplotlib.lines.Line2D object at 0x000001D113F57B10>, <matplotlib.lines.Line2D object at 0x000001D113F57C50>], 'boxes': [<matplotlib.patches.PathPatch object at 0x000001D113F07770>], 'medians': [<matplotlib.lines.Line2D object at 0x000001D113F57D90>], 'fliers': [<matplotlib.lines.Line2D object at 0x000001D113FA4050>], 'means': [<matplotlib.lines.Line2D object at 0x000001D113F57ED0>]}
plt.xlabel('Columns')
Text(0.5, 0, 'Columns')
plt.ylabel('Price')
Text(0, 0.5, 'Price')
plt.show()
plt.boxplot(df2['Weight_kg'])
{'whiskers': [<matplotlib.lines.Line2D object at 0x000001D11432C2D0>, <matplotlib.lines.Line2D object at 0x000001D11432C410>], 'caps': [<matplotlib.lines.Line2D object at 0x000001D11432C550>, <matplotlib.lines.Line2D object at 0x000001D11432C690>], 'boxes': [<matplotlib.lines.Line2D object at 0x000001D11432C190>], 'medians': [<matplotlib.lines.Line2D object at 0x000001D11432C7D0>], 'fliers': [<matplotlib.lines.Line2D object at 0x000001D11432C910>], 'means': []}
>>> plt.xlabel('Columns')
Text(0.5, 0, 'Columns')
>>> plt.ylabel('Weight_kg')
Text(0, 0.5, 'Weight_kg')
>>> plt.show()
>>> KeyboardInterrupt
>>> import seaborn as sns
>>> sns.boxplot(df2['Weight_kg'])
<Axes: ylabel='Weight_kg'>
>>> plt.show()
>>> sns.boxplot(x = df2['Weight_kg'], y = df2['RAM'])
<Axes: xlabel='Weight_kg', ylabel='RAM'>
>>> plt.show()
>>> 
>>> 
>>> #12B
>>> import pandas as pd
>>> data = pd.read_csv("C:/Users/Chandu/Downloads/10prog_4laptops.csv")
>>> data
    Manufacturer       Model_Name  ... Weight_kg        Price
0          Apple      MacBook Pro  ...      1.37  11912523.48
1          Apple      Macbook Air  ...      1.34   7993374.48
2             HP           250 G6  ...      1.86   5112900.00
3          Apple      MacBook Pro  ...      1.83  22563005.40
4          Apple      MacBook Pro  ...      1.37  16037611.20
..           ...              ...  ...       ...          ...
972         Dell     Alienware 17  ...      4.42  24897600.00
973      Toshiba  Tecra A40-C-1DF  ...      1.95  10492560.00
974         Asus        Rog Strix  ...      2.73  18227710.80
975           HP      Probook 450  ...      2.04   8705268.00
976       Lenovo    ThinkPad T460  ...      1.70   8909784.00

[977 rows x 13 columns]
>>> q3 = data['Weight_kg'].quantile(0.75)
>>> q1 = data['Weight_kg'].quantile(0.25)
>>> iqr = q3 - q1
>>> lower_bound = q1 - 1.5*iqr
>>> upper_bound = q3 + 1.5*iqr
>>> outliers = data[(data['Weight_kg'] < lower_bound) | (data['Weight_kg'] > upper_bound)]
>>> print('lower bound, upper bound and iqr values are: ',lower_bound, upper_bound,iqr)
lower bound, upper bound and iqr values are:  0.30000000000000027 3.4999999999999996 0.7999999999999998
>>> print('No.of outliers are: ', outliers.shape[0])
No.of outliers are:  33
