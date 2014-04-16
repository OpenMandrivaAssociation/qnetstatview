Summary:	Shows detailed listings of all TCP and UDP endpoints
Name:		qnetstatview
Version:	1.2.0
Release:	6
License:	GPLv3+
Group:		Networking/Other
Url:		http://qt-apps.org/content/show.php?content=157088
Source0:	http://dansoft.krasnokamensk.ru/data/1016/qnetstatview_source.tar.gz
BuildRequires:	imagemagick
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRequires:	qt4-devel

%description
Shows detailed listings of all TCP and UDP endpoints.

#----------------------------------------------------------------------------

%files
%doc Bin/HISTORY Bin/COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png


%prep
%setup -q -n %{name}_source
find . -perm 0600 | xargs chmod 0644

%build
%qmake_qt4 QMAKE_CXXFLAGS_RELEASE= %{name}.pro
%make

%install
# install binary
mkdir -p %{buildroot}%{_bindir}
cp Bin/%{name} %{buildroot}%{_bindir}/%{name}

# install locales
mkdir -p %{buildroot}%{_datadir}/%{name}
cp Bin/*.qm %{buildroot}%{_datadir}/%{name}/

# create and install icons
for N in 16 32 48 64 128; do convert %{name}.ico -scale ${N}x${N}! $N.png; done
install -D 16.png -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -D 32.png -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -D 48.png -m 644 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -D 64.png -m 644 %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D 128.png -m 644 %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# XDG menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=QNetStatView
Comment=Shows detailed listings of all TCP and UDP endpoints
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Network;Utility;
EOF

