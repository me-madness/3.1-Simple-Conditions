size = float(input())
metric_in = input().lower()
metric_out = input().lower()

if metric_in == 'mm':
    size = size * 1000
elif metric_in == 'cm':
    size = size * 100
elif metric_in == 'mi':
    size = size / 0.000621371192
elif metric_in == 'in':
    size = size * 39.3700787
elif metric_in == 'km':
    size = size / 0.001        
elif metric_in == 'ft':
    size = size * 3.2808399
else:
    size = size * 1.0936133
 
if metric_out == 'mm':
    size = size * 1000
elif metric_out == 'cm':
    size = size * 100
elif metric_out == 'mi':
    size = size / 0.000621371192
elif metric_out == 'in':
    size = size * 39.3700787
elif metric_out == 'km':
    size = size * 0.001        
elif metric_out == 'ft':
    size = size * 3.2808399
else:
    size = size * 1.0936133     

print(size)



# 1 meter (m)1000 millimeters (mm)
# 1 meter (m)100 centimeters (cm)
# 1 meter (m)0.000621371192 miles (mi)
# 1 meter (m)39.3700787 inches (in)
# 1 meter (m)0.001 kilometers (km)
# 1 meter (m)3.2808399 feet (ft)
# 1 meter (m)1.0936133 yards (yd)