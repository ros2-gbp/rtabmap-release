Name:           ros-hydro-rtabmap
Version:        0.7.1
Release:        1%{?dist}
Summary:        ROS rtabmap package

Group:          Development/Libraries
License:        BSD
URL:            http://introlab.github.io/rtabmap
Source0:        %{name}-%{version}.tar.gz

Requires:       libsq3-devel
Requires:       pcl-devel
Requires:       qt-devel
Requires:       ros-hydro-cv-bridge
Requires:       zlib-devel
BuildRequires:  cmake
BuildRequires:  libsq3-devel
BuildRequires:  pcl-devel
BuildRequires:  qt-devel
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  zlib-devel

%description
The rtabmap standalone library

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Nov 25 2014 Mathieu Labbe <matlabbe@gmail.com> - 0.7.1-1
- Autogenerated by Bloom

