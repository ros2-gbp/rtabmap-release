%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-rtabmap
Version:        0.21.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rtabmap package

License:        BSD
URL:            http://introlab.github.io/rtabmap
Source0:        %{name}-%{version}.tar.gz

Requires:       libfreenect-devel
Requires:       libsq3-devel
Requires:       openni-devel
Requires:       pcl-devel
Requires:       ros-humble-cv-bridge
Requires:       ros-humble-libg2o
Requires:       ros-humble-libpointmatcher
Requires:       ros-humble-octomap
Requires:       ros-humble-qt-gui-cpp
Requires:       zlib-devel
Requires:       ros-humble-ros-workspace
BuildRequires:  cmake3
BuildRequires:  libfreenect-devel
BuildRequires:  libsq3-devel
BuildRequires:  openni-devel
BuildRequires:  pcl-devel
BuildRequires:  proj-devel
BuildRequires:  ros-humble-cv-bridge
BuildRequires:  ros-humble-libg2o
BuildRequires:  ros-humble-libpointmatcher
BuildRequires:  ros-humble-octomap
BuildRequires:  ros-humble-qt-gui-cpp
BuildRequires:  zlib-devel
BuildRequires:  ros-humble-ros-workspace
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Sun Apr 09 2023 Mathieu Labbe <matlabbe@gmail.com> - 0.21.1-1
- Autogenerated by Bloom

* Sun Jan 22 2023 Mathieu Labbe <matlabbe@gmail.com> - 0.20.23-1
- Autogenerated by Bloom

* Sun Dec 11 2022 Mathieu Labbe <matlabbe@gmail.com> - 0.20.22-1
- Autogenerated by Bloom

* Sat Oct 01 2022 Mathieu Labbe <matlabbe@gmail.com> - 0.20.21-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Mathieu Labbe <matlabbe@gmail.com> - 0.20.18-2
- Autogenerated by Bloom

