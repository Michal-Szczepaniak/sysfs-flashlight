Name:       sysfs-flashlight
Summary:    sysfs flashlight D-Bus service
Version:    1.0.0
Release:    1
License:    Apache-2.0
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
BuildRequires: systemd
Requires:   python3-dbus
Requires:   python3-gobject
Requires:   systemd
Provides:   sailfish-flashlight-provider
Conflicts:  droidmedia-flashlight

%description
Provides org.sailfish.flashlight.provider on the session bus and switches the
torch through /sys/kernel/debug/ledflash. Replaces droidmedia-flashlight,
which goes through the Android camera stack.

%prep
%setup -q -n %{name}-%{version}

%build

%install
install -D -m 755 sysfs-flashlight %{buildroot}%{_bindir}/sysfs-flashlight
install -D -m 644 org.sailfish.flashlight.provider.service \
    %{buildroot}%{_datadir}/dbus-1/services/org.sailfish.flashlight.provider.service

%files
%{_bindir}/sysfs-flashlight
%{_datadir}/dbus-1/services/org.sailfish.flashlight.provider.service
