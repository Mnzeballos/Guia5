echo "para correr los programas de forma secuencial:"
python3 eje5a.py 10 
python3 eje5b.py 11 
python3 eje5c.py 12

echo "para correr los programas de forma simultanea:"
python3 eje5a.py 10 &
python3 eje5b.py 11 &
python3 eje5c.py 12
wait