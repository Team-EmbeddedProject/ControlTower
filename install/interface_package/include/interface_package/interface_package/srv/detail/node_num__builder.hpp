// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interface_package:srv/NodeNum.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__BUILDER_HPP_
#define INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interface_package/srv/detail/node_num__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interface_package
{

namespace srv
{

namespace builder
{

class Init_NodeNum_Request_next_y
{
public:
  explicit Init_NodeNum_Request_next_y(::interface_package::srv::NodeNum_Request & msg)
  : msg_(msg)
  {}
  ::interface_package::srv::NodeNum_Request next_y(::interface_package::srv::NodeNum_Request::_next_y_type arg)
  {
    msg_.next_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface_package::srv::NodeNum_Request msg_;
};

class Init_NodeNum_Request_next_x
{
public:
  explicit Init_NodeNum_Request_next_x(::interface_package::srv::NodeNum_Request & msg)
  : msg_(msg)
  {}
  Init_NodeNum_Request_next_y next_x(::interface_package::srv::NodeNum_Request::_next_x_type arg)
  {
    msg_.next_x = std::move(arg);
    return Init_NodeNum_Request_next_y(msg_);
  }

private:
  ::interface_package::srv::NodeNum_Request msg_;
};

class Init_NodeNum_Request_current_y
{
public:
  explicit Init_NodeNum_Request_current_y(::interface_package::srv::NodeNum_Request & msg)
  : msg_(msg)
  {}
  Init_NodeNum_Request_next_x current_y(::interface_package::srv::NodeNum_Request::_current_y_type arg)
  {
    msg_.current_y = std::move(arg);
    return Init_NodeNum_Request_next_x(msg_);
  }

private:
  ::interface_package::srv::NodeNum_Request msg_;
};

class Init_NodeNum_Request_current_x
{
public:
  Init_NodeNum_Request_current_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NodeNum_Request_current_y current_x(::interface_package::srv::NodeNum_Request::_current_x_type arg)
  {
    msg_.current_x = std::move(arg);
    return Init_NodeNum_Request_current_y(msg_);
  }

private:
  ::interface_package::srv::NodeNum_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface_package::srv::NodeNum_Request>()
{
  return interface_package::srv::builder::Init_NodeNum_Request_current_x();
}

}  // namespace interface_package


namespace interface_package
{

namespace srv
{

namespace builder
{

class Init_NodeNum_Response_success
{
public:
  Init_NodeNum_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interface_package::srv::NodeNum_Response success(::interface_package::srv::NodeNum_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface_package::srv::NodeNum_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface_package::srv::NodeNum_Response>()
{
  return interface_package::srv::builder::Init_NodeNum_Response_success();
}

}  // namespace interface_package

#endif  // INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__BUILDER_HPP_
