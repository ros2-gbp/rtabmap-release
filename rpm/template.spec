%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rtabmap
Version:        0.21.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rtabmap package

License:        BSD
URL:            http://introlab.github.io/rtabmap
Source0:        %{name}-%{version}.tar.gz

Requires:       libsq3-devel
Requires:       pcl-devel
Requires:       ros-iron-cv-bridge
Requires:       ros-iron-grid-map-core
Requires:       ros-iron-gtsam
Requires:       ros-iron-libg2o
Requires:       ros-iron-libpointmatcher
Requires:       ros-iron-octomap
Requires:       ros-iron-qt-gui-cpp
Requires:       zlib-devel
Requires:       ros-iron-ros-workspace
BuildRequires:  cmake3
BuildRequires:  libsq3-devel
BuildRequires:  pcl-devel
BuildRequires:  proj-devel
BuildRequires:  ros-iron-cv-bridge
BuildRequires:  ros-iron-grid-map-core
BuildRequires:  ros-iron-gtsam
BuildRequires:  ros-iron-libg2o
BuildRequires:  ros-iron-libpointmatcher
BuildRequires:  ros-iron-octomap
BuildRequires:  ros-iron-qt-gui-cpp
BuildRequires:  zlib-devel
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
RTAB-Map's standalone library. RTAB-Map is a RGB-D SLAM approach with real-time
constraints.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
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
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Sun Jun 30 2024 Mathieu Labbe <matlabbe@gmail.com> - 0.21.5-1
- Autogenerated by Bloom

* Tue Feb 20 2024 Mathieu Labbe <matlabbe@gmail.com> - 0.21.4-1
- Autogenerated by Bloom

* Thu Jan 04 2024 Mathieu Labbe <matlabbe@gmail.com> - 0.21.3-1
- Autogenerated by Bloom

* Sat Aug 05 2023 Mathieu Labbe <matlabbe@gmail.com> - 0.21.2-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Mathieu Labbe <matlabbe@gmail.com> - 0.21.1-3
- Autogenerated by Bloom

* Sun Apr 09 2023 Mathieu Labbe <matlabbe@gmail.com> - 0.21.1-2
- Autogenerated by Bloom

* Sun Apr 09 2023 Mathieu Labbe <matlabbe@gmail.com> - 0.21.1-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Mathieu Labbe <matlabbe@gmail.com> - 0.20.23-2
- Autogenerated by Bloom

