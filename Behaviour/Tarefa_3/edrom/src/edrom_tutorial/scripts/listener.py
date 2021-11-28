
import rospy
from std_msgs.msg import String

def callback(data):
    
    print(data)

def listener():
    	
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    
    

    rospy.spin()

if __name__ == '__main__':
    rospy.loginfo("Rodando")
    listener()
