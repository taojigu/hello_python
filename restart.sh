 ps aux | grep python | grep -v "grep python" | awk '{print $2}' | xargs sudo kill -9

nohup python3 -u main_web.py params1 > nohupWeb.out 2>&1 &
nohup python3 -u main_food.py params1 > nohupFood.out 2>&1 &