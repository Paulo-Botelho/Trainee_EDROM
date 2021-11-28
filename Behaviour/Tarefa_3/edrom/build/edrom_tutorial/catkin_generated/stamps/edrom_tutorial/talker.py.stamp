import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rospy.loginfo("Oi")
    while not rospy.is_shutdown():
        pub.publish(input("Coordenada x: ")
                
        print("Tamanho do plano cartesiano em x vai de -500 a 500")
        x =int(input("Coordenada x: "))
        print("Tamanho do plano cartesiano em y vai de -500 a 500")
        y = int(input("Coordenada y: "))
        
        if x > 500 or y > 500 or x < -500 or y < -500:
        	print("As coordenadas estão fora do plano cartesiano")
        	exit()
        else:

        	if x <= 500 and x > 0:
            		x_sit = "a direita"
        	elif x < 0 and x >= -500:
            		x_sit = "a esquerda"
        	elif x == 0:
            		x_sit = "ao centro"
        
        	if y <= 500 and y > 0:
            		y_sit = "emcima"
        	elif y < 0 and y >= -500:
            		y_sit = "embaixo"
        	elif y == 0:
            		y_sit = "ao centro"
        
        data = x_sit + y_sit
        pub.publish(data)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
