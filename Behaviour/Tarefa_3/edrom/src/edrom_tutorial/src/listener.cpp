#include "ros/ros.h"
#include "edrom_tutorial/edrom_message.h"

void chatterCallback(const edrom_tutorial::edrom_message::ConstPtr& msg)
{
    ROS_INFO("Eu ouvi [%s]", msg->str.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "listener");
    ros::NodeHandle node;

    ros::Subscriber subscriber  = node.subscribe("chatter", 10, chatterCallback);

    ros::spin();
    return 0;
}
