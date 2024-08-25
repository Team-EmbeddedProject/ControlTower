// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interface_package:srv/NodeNum.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__TRAITS_HPP_
#define INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interface_package/srv/detail/node_num__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interface_package
{

namespace srv
{

inline void to_flow_style_yaml(
  const NodeNum_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: current_x
  {
    out << "current_x: ";
    rosidl_generator_traits::value_to_yaml(msg.current_x, out);
    out << ", ";
  }

  // member: current_y
  {
    out << "current_y: ";
    rosidl_generator_traits::value_to_yaml(msg.current_y, out);
    out << ", ";
  }

  // member: next_x
  {
    out << "next_x: ";
    rosidl_generator_traits::value_to_yaml(msg.next_x, out);
    out << ", ";
  }

  // member: next_y
  {
    out << "next_y: ";
    rosidl_generator_traits::value_to_yaml(msg.next_y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const NodeNum_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: current_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_x: ";
    rosidl_generator_traits::value_to_yaml(msg.current_x, out);
    out << "\n";
  }

  // member: current_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_y: ";
    rosidl_generator_traits::value_to_yaml(msg.current_y, out);
    out << "\n";
  }

  // member: next_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "next_x: ";
    rosidl_generator_traits::value_to_yaml(msg.next_x, out);
    out << "\n";
  }

  // member: next_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "next_y: ";
    rosidl_generator_traits::value_to_yaml(msg.next_y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NodeNum_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interface_package

namespace rosidl_generator_traits
{

[[deprecated("use interface_package::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interface_package::srv::NodeNum_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interface_package::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interface_package::srv::to_yaml() instead")]]
inline std::string to_yaml(const interface_package::srv::NodeNum_Request & msg)
{
  return interface_package::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interface_package::srv::NodeNum_Request>()
{
  return "interface_package::srv::NodeNum_Request";
}

template<>
inline const char * name<interface_package::srv::NodeNum_Request>()
{
  return "interface_package/srv/NodeNum_Request";
}

template<>
struct has_fixed_size<interface_package::srv::NodeNum_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interface_package::srv::NodeNum_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interface_package::srv::NodeNum_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace interface_package
{

namespace srv
{

inline void to_flow_style_yaml(
  const NodeNum_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const NodeNum_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NodeNum_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interface_package

namespace rosidl_generator_traits
{

[[deprecated("use interface_package::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interface_package::srv::NodeNum_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interface_package::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interface_package::srv::to_yaml() instead")]]
inline std::string to_yaml(const interface_package::srv::NodeNum_Response & msg)
{
  return interface_package::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interface_package::srv::NodeNum_Response>()
{
  return "interface_package::srv::NodeNum_Response";
}

template<>
inline const char * name<interface_package::srv::NodeNum_Response>()
{
  return "interface_package/srv/NodeNum_Response";
}

template<>
struct has_fixed_size<interface_package::srv::NodeNum_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interface_package::srv::NodeNum_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interface_package::srv::NodeNum_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interface_package::srv::NodeNum>()
{
  return "interface_package::srv::NodeNum";
}

template<>
inline const char * name<interface_package::srv::NodeNum>()
{
  return "interface_package/srv/NodeNum";
}

template<>
struct has_fixed_size<interface_package::srv::NodeNum>
  : std::integral_constant<
    bool,
    has_fixed_size<interface_package::srv::NodeNum_Request>::value &&
    has_fixed_size<interface_package::srv::NodeNum_Response>::value
  >
{
};

template<>
struct has_bounded_size<interface_package::srv::NodeNum>
  : std::integral_constant<
    bool,
    has_bounded_size<interface_package::srv::NodeNum_Request>::value &&
    has_bounded_size<interface_package::srv::NodeNum_Response>::value
  >
{
};

template<>
struct is_service<interface_package::srv::NodeNum>
  : std::true_type
{
};

template<>
struct is_service_request<interface_package::srv::NodeNum_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interface_package::srv::NodeNum_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__TRAITS_HPP_
