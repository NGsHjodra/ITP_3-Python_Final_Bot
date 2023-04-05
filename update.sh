sudo docker compose down
sudo docker compose up -d --build
pip install -r requirements.txt
echo "Sleeping for 10 seconds to allow the database to start up..."
sleep 10
sudo docker ps
python3 test-db.py
python3 read-db.py