echo "para correr los programas de forma secuencial:"
python3 eje5a.py 20 
python3 eje5b.py 21 
python3 eje5c.py 22

echo "para correr los programas de forma simultanea:"
python3 eje5a.py 20 &
python3 eje5b.py 21 &
python3 eje5c.py 22
wait