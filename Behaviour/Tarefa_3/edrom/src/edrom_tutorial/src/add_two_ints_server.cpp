#include "ros/ros.h"
#include "edrom_tutorial/GrausParaMotor.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "graus_para_motor_client");
  if (argc != 2)
  {
    ROS_INFO("usage: graus_para_motor_client Graus");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<edrom_tutorial::GrausParaMotor>("graus_para_motor");
  edrom_tutorial::GrausParaMotor srv;
  srv.request.graus = atoll(argv[1]);
  if (client.call(srv))
  {
    ROS_INFO("Motor: %f", (float)srv.response.motor);
  }
  else
  {
    ROS_ERROR("Failed to call service graus_para_motor");
    return 1;
  }

  return 0;
}
