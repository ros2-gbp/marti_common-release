%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/kilted/.*$
%global __requires_exclude_from ^/opt/ros/kilted/.*$

Name:           ros-kilted-swri-transform-util
Version:        3.7.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS swri_transform_util package

License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       GeographicLib-devel
Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       geos-devel
Requires:       proj-devel
Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-yaml
Requires:       ros-kilted-cv-bridge
Requires:       ros-kilted-diagnostic-msgs
Requires:       ros-kilted-diagnostic-updater
Requires:       ros-kilted-geographic-msgs
Requires:       ros-kilted-geometry-msgs
Requires:       ros-kilted-gps-msgs
Requires:       ros-kilted-marti-nav-msgs
Requires:       ros-kilted-rcl-interfaces
Requires:       ros-kilted-rclcpp
Requires:       ros-kilted-rclcpp-components
Requires:       ros-kilted-rclpy
Requires:       ros-kilted-sensor-msgs
Requires:       ros-kilted-swri-math-util
Requires:       ros-kilted-swri-roscpp
Requires:       ros-kilted-tf2
Requires:       ros-kilted-tf2-geometry-msgs
Requires:       ros-kilted-tf2-ros
Requires:       yaml-cpp-devel
Requires:       ros-kilted-ros-workspace
BuildRequires:  GeographicLib-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  geos-devel
BuildRequires:  pkgconfig
BuildRequires:  proj-devel
BuildRequires:  ros-kilted-ament-cmake
BuildRequires:  ros-kilted-ament-cmake-python
BuildRequires:  ros-kilted-cv-bridge
BuildRequires:  ros-kilted-diagnostic-msgs
BuildRequires:  ros-kilted-diagnostic-updater
BuildRequires:  ros-kilted-geographic-msgs
BuildRequires:  ros-kilted-geometry-msgs
BuildRequires:  ros-kilted-gps-msgs
BuildRequires:  ros-kilted-marti-nav-msgs
BuildRequires:  ros-kilted-rcl-interfaces
BuildRequires:  ros-kilted-rclcpp
BuildRequires:  ros-kilted-rclcpp-components
BuildRequires:  ros-kilted-rclpy
BuildRequires:  ros-kilted-sensor-msgs
BuildRequires:  ros-kilted-swri-math-util
BuildRequires:  ros-kilted-swri-roscpp
BuildRequires:  ros-kilted-tf2
BuildRequires:  ros-kilted-tf2-geometry-msgs
BuildRequires:  ros-kilted-tf2-ros
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-kilted-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-kilted-ament-cmake-gtest
BuildRequires:  ros-kilted-ament-index-cpp
BuildRequires:  ros-kilted-launch-ros
BuildRequires:  ros-kilted-launch-testing
BuildRequires:  ros-kilted-launch-testing-ament-cmake
%endif

%description
The swri_transform_util package contains utility functions and classes for
transforming between coordinate frames.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/kilted" \
    -DAMENT_PREFIX_PATH="/opt/ros/kilted" \
    -DCMAKE_PREFIX_PATH="/opt/ros/kilted" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/kilted

%changelog
* Tue May 20 2025 Southwest Research Institute <swri-robotics@swri.org> - 3.7.5-1
- Autogenerated by Bloom

* Tue May 20 2025 Southwest Research Institute <swri-robotics@swri.org> - 3.7.4-3
- Autogenerated by Bloom

* Tue Apr 22 2025 Southwest Research Institute <swri-robotics@swri.org> - 3.7.4-2
- Autogenerated by Bloom

* Mon Apr 14 2025 Southwest Research Institute <swri-robotics@swri.org> - 3.7.4-1
- Autogenerated by Bloom

* Wed Sep 18 2024 Southwest Research Institute <swri-robotics@swri.org> - 3.7.3-1
- Autogenerated by Bloom

* Mon Sep 16 2024 Southwest Research Institute <swri-robotics@swri.org> - 3.7.2-1
- Autogenerated by Bloom

* Fri Sep 06 2024 Southwest Research Institute <swri-robotics@swri.org> - 3.7.1-1
- Autogenerated by Bloom

* Wed Mar 06 2024 P. J. Reed <preed@swri.org> - 3.6.1-2
- Autogenerated by Bloom

