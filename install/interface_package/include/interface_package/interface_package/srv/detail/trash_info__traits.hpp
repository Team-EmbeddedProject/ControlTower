// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interface_package:srv/TrashInfo.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__SRV__DETAIL__TRASH_INFO__TRAITS_HPP_
#define INTERFACE_PACKAGE__SRV__DETAIL__TRASH_INFO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interface_package/srv/detail/trash_info__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace interface_package
{

namespace srv
{

inline void to_flow_style_yaml(
  const TrashInfo_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    to_flow_style_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: robot_id
  {
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << ", ";
  }

  // member: trash_type
  {
    out << "trash_type: ";
    rosidl_generator_traits::value_to_yaml(msg.trash_type, out);
    out << ", ";
  }

  // member: latitude
  {
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << ", ";
  }

  // member: longitude
  {
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TrashInfo_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp:\n";
    to_block_style_yaml(msg.timestamp, out, indentation + 2);
  }

  // member: robot_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << "\n";
  }

  // member: trash_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "trash_type: ";
    rosidl_generator_traits::value_to_yaml(msg.trash_type, out);
    out << "\n";
  }

  // member: latitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << "\n";
  }

  // member: longitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TrashInfo_Request & msg, bool use_flow_style = false)
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
  const interface_package::srv::TrashInfo_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interface_package::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interface_package::srv::to_yaml() instead")]]
inline std::string to_yaml(const interface_package::srv::TrashInfo_Request & msg)
{
  return interface_package::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interface_package::srv::TrashInfo_Request>()
{
  return "interface_package::srv::TrashInfo_Request";
}

template<>
inline const char * name<interface_package::srv::TrashInfo_Request>()
{
  return "interface_package/srv/TrashInfo_Request";
}

template<>
struct has_fixed_size<interface_package::srv::TrashInfo_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interface_package::srv::TrashInfo_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<interface_package::srv::TrashInfo_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace interface_package
{

namespace srv
{

inline void to_flow_style_yaml(
  const TrashInfo_Response & msg,
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
  const TrashInfo_Response & msg,
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

inline std::string to_yaml(const TrashInfo_Response & msg, bool use_flow_style = false)
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
  const interface_package::srv::TrashInfo_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interface_package::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interface_package::srv::to_yaml() instead")]]
inline std::string to_yaml(const interface_package::srv::TrashInfo_Response & msg)
{
  return interface_package::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interface_package::srv::TrashInfo_Response>()
{
  return "interface_package::srv::TrashInfo_Response";
}

template<>
inline const char * name<interface_package::srv::TrashInfo_Response>()
{
  return "interface_package/srv/TrashInfo_Response";
}

template<>
struct has_fixed_size<interface_package::srv::TrashInfo_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interface_package::srv::TrashInfo_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interface_package::srv::TrashInfo_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interface_package::srv::TrashInfo>()
{
  return "interface_package::srv::TrashInfo";
}

template<>
inline const char * name<interface_package::srv::TrashInfo>()
{
  return "interface_package/srv/TrashInfo";
}

template<>
struct has_fixed_size<interface_package::srv::TrashInfo>
  : std::integral_constant<
    bool,
    has_fixed_size<interface_package::srv::TrashInfo_Request>::value &&
    has_fixed_size<interface_package::srv::TrashInfo_Response>::value
  >
{
};

template<>
struct has_bounded_size<interface_package::srv::TrashInfo>
  : std::integral_constant<
    bool,
    has_bounded_size<interface_package::srv::TrashInfo_Request>::value &&
    has_bounded_size<interface_package::srv::TrashInfo_Response>::value
  >
{
};

template<>
struct is_service<interface_package::srv::TrashInfo>
  : std::true_type
{
};

template<>
struct is_service_request<interface_package::srv::TrashInfo_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interface_package::srv::TrashInfo_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACE_PACKAGE__SRV__DETAIL__TRASH_INFO__TRAITS_HPP_
