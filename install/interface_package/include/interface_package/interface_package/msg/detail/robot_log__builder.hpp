// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interface_package:msg/RobotLog.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__MSG__DETAIL__ROBOT_LOG__BUILDER_HPP_
#define INTERFACE_PACKAGE__MSG__DETAIL__ROBOT_LOG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interface_package/msg/detail/robot_log__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interface_package
{

namespace msg
{

namespace builder
{

class Init_RobotLog_status
{
public:
  explicit Init_RobotLog_status(::interface_package::msg::RobotLog & msg)
  : msg_(msg)
  {}
  ::interface_package::msg::RobotLog status(::interface_package::msg::RobotLog::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface_package::msg::RobotLog msg_;
};

class Init_RobotLog_longitude
{
public:
  explicit Init_RobotLog_longitude(::interface_package::msg::RobotLog & msg)
  : msg_(msg)
  {}
  Init_RobotLog_status longitude(::interface_package::msg::RobotLog::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_RobotLog_status(msg_);
  }

private:
  ::interface_package::msg::RobotLog msg_;
};

class Init_RobotLog_latitude
{
public:
  explicit Init_RobotLog_latitude(::interface_package::msg::RobotLog & msg)
  : msg_(msg)
  {}
  Init_RobotLog_longitude latitude(::interface_package::msg::RobotLog::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_RobotLog_longitude(msg_);
  }

private:
  ::interface_package::msg::RobotLog msg_;
};

class Init_RobotLog_robot_id
{
public:
  explicit Init_RobotLog_robot_id(::interface_package::msg::RobotLog & msg)
  : msg_(msg)
  {}
  Init_RobotLog_latitude robot_id(::interface_package::msg::RobotLog::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_RobotLog_latitude(msg_);
  }

private:
  ::interface_package::msg::RobotLog msg_;
};

class Init_RobotLog_timestamp
{
public:
  Init_RobotLog_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotLog_robot_id timestamp(::interface_package::msg::RobotLog::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_RobotLog_robot_id(msg_);
  }

private:
  ::interface_package::msg::RobotLog msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface_package::msg::RobotLog>()
{
  return interface_package::msg::builder::Init_RobotLog_timestamp();
}

}  // namespace interface_package

#endif  // INTERFACE_PACKAGE__MSG__DETAIL__ROBOT_LOG__BUILDER_HPP_
