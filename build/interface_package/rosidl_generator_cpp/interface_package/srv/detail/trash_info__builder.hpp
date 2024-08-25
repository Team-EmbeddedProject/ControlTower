// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interface_package:srv/TrashInfo.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__SRV__DETAIL__TRASH_INFO__BUILDER_HPP_
#define INTERFACE_PACKAGE__SRV__DETAIL__TRASH_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interface_package/srv/detail/trash_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interface_package
{

namespace srv
{

namespace builder
{

class Init_TrashInfo_Request_longitude
{
public:
  explicit Init_TrashInfo_Request_longitude(::interface_package::srv::TrashInfo_Request & msg)
  : msg_(msg)
  {}
  ::interface_package::srv::TrashInfo_Request longitude(::interface_package::srv::TrashInfo_Request::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface_package::srv::TrashInfo_Request msg_;
};

class Init_TrashInfo_Request_latitude
{
public:
  explicit Init_TrashInfo_Request_latitude(::interface_package::srv::TrashInfo_Request & msg)
  : msg_(msg)
  {}
  Init_TrashInfo_Request_longitude latitude(::interface_package::srv::TrashInfo_Request::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_TrashInfo_Request_longitude(msg_);
  }

private:
  ::interface_package::srv::TrashInfo_Request msg_;
};

class Init_TrashInfo_Request_trash_type
{
public:
  explicit Init_TrashInfo_Request_trash_type(::interface_package::srv::TrashInfo_Request & msg)
  : msg_(msg)
  {}
  Init_TrashInfo_Request_latitude trash_type(::interface_package::srv::TrashInfo_Request::_trash_type_type arg)
  {
    msg_.trash_type = std::move(arg);
    return Init_TrashInfo_Request_latitude(msg_);
  }

private:
  ::interface_package::srv::TrashInfo_Request msg_;
};

class Init_TrashInfo_Request_robot_id
{
public:
  explicit Init_TrashInfo_Request_robot_id(::interface_package::srv::TrashInfo_Request & msg)
  : msg_(msg)
  {}
  Init_TrashInfo_Request_trash_type robot_id(::interface_package::srv::TrashInfo_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_TrashInfo_Request_trash_type(msg_);
  }

private:
  ::interface_package::srv::TrashInfo_Request msg_;
};

class Init_TrashInfo_Request_timestamp
{
public:
  Init_TrashInfo_Request_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrashInfo_Request_robot_id timestamp(::interface_package::srv::TrashInfo_Request::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_TrashInfo_Request_robot_id(msg_);
  }

private:
  ::interface_package::srv::TrashInfo_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface_package::srv::TrashInfo_Request>()
{
  return interface_package::srv::builder::Init_TrashInfo_Request_timestamp();
}

}  // namespace interface_package


namespace interface_package
{

namespace srv
{

namespace builder
{

class Init_TrashInfo_Response_success
{
public:
  Init_TrashInfo_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interface_package::srv::TrashInfo_Response success(::interface_package::srv::TrashInfo_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface_package::srv::TrashInfo_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface_package::srv::TrashInfo_Response>()
{
  return interface_package::srv::builder::Init_TrashInfo_Response_success();
}

}  // namespace interface_package

#endif  // INTERFACE_PACKAGE__SRV__DETAIL__TRASH_INFO__BUILDER_HPP_
