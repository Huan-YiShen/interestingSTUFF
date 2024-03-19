if [ -f clib_cal.so ]; then
    rm clib_cal.so
fi

gcc -Wall -fPIC -shared -o clib_cal.so clib_cal.c
