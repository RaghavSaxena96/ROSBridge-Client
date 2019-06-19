import websocket
import WebsocketROSClient 
from geometry_msgs.msg import Twist, PoseStamped

ws_client = WebsocketROSClient.ws_client('127.0.0.1', 9090) # ip, port, name of client
ws_client.connect()

vel_msg = Twist()
vel_msg.linear.x = 0.2
vel_msg.linear.y = 0.3
vel_msg.linear.z = 0.4
vel_msg.angular.x = 0.3
vel_msg.angular.y = 0.4
vel_msg.angular.z = 0.5
# 1. the name of the topic on server where to publish; 
# 2. the message



ws_client.publish("/cmd_vel",vel_msg)


