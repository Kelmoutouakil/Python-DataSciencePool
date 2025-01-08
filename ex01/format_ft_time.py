# >python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
import time
from datetime import datetime
#get current Unix timestamp with fractions of seconds
current = time.time()
#get scientific notation
scientific_notation = f"{current:.2e}"
#convert the timestamp to human readable format but we should use the datetime.utcfromtimestamp to convert the float the timestamp to a datetime 
#object first then we can use the method strftime 
read = datetime.utcfromtimestamp(current).strftime("%b %d %Y")
print(f"Seconds since January 1, 1970: {current} or {scientific_notation} in scientific notation")
print(read)

