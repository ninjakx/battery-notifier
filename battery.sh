function myfunc()
{
battery_level = 'acpi -b | cut -d"," -f2'
}

myfunc
echo $battery_level    
