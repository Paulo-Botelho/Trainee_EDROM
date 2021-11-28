#include "ros/ros.h"
#include "edrom_tutorial/edrom_message.h"

int main(int argc, char **argv) {
    ros::init(argc, argv, "talker");
    ros::NodeHandle nh;
    ros::Publisher chatterPublisher = nh.advertise<edrom_tutorial::edrom_message>("chatter", 1);
    ros::Rate loopRate(10);
    edrom_tutorial::edrom_message msg;
    unsigned int count = 0;

    while(ros::ok()) {
        std::stringstream ss;
        ss << "Bem-vindo a edrom " << count;
        msg.str = ss.str();
        ROS_INFO_STREAM(msg.str);
        chatterPublisher.publish(msg);
        ros::spinOnce();
        loopRate.sleep();
        count++;
        }
    return 0;
}
