%global debug_package %{nil}
%define _version_long 20240203-110809-5046fc22

Name: wezterm
Version: 20240203
Release: 110809.5046fc22
Summary: Wez's Terminal Emulator.
License: MIT
URL: https://github.com/wezterm/%{name}
Source: %{url}/archive/refs/tags/%{_version_long}.tar.gz

BuildRequires: cargo
BuildRequires: curl
BuildRequires: fontconfig-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: make
BuildRequires: mesa-libEGL-devel
BuildRequires: openssl-devel
BuildRequires: openssl-devel-engine
BuildRequires: rust
BuildRequires: wayland-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-wm-devel

Requires: dbus
Requires: fontconfig
Requires: libwayland-client
Requires: libwayland-cursor
Requires: libwayland-egl
Requires: libxcb
Requires: libxkbcommon
Requires: libxkbcommon-x11
Requires: mesa-libEGL
Requires: openssl
Requires: xcb-util-keysyms
Requires: xcb-util-wm

%description

%prep
%autosetup -n %{name}-%{_version_long}

%build
cargo build --release -p wezterm-gui -p wezterm -p wezterm-mux-server -p strip-ansi-escapes

%install
mkdir -p %{buildroot}/usr/bin %{buildroot}/etc/profile.d
install -Dm755 assets/open-wezterm-here -t %{buildroot}/usr/bin
install -Dsm755 target/release/wezterm -t %{buildroot}/usr/bin
install -Dsm755 target/release/wezterm-mux-server -t %{buildroot}/usr/bin
install -Dsm755 target/release/wezterm-gui -t %{buildroot}/usr/bin
install -Dsm755 target/release/strip-ansi-escapes -t %{buildroot}/usr/bin
install -Dm644 assets/shell-integration/* -t %{buildroot}/etc/profile.d
install -Dm644 assets/shell-completion/zsh %{buildroot}/usr/share/zsh/site-functions/_wezterm
install -Dm644 assets/shell-completion/bash %{buildroot}/etc/bash_completion.d/wezterm
install -Dm644 assets/icon/terminal.png %{buildroot}/usr/share/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
install -Dm644 assets/wezterm.desktop %{buildroot}/usr/share/applications/org.wezfurlong.wezterm.desktop
install -Dm644 assets/wezterm.appdata.xml %{buildroot}/usr/share/metainfo/org.wezfurlong.wezterm.appdata.xml
install -Dm644 assets/wezterm-nautilus.py %{buildroot}/usr/share/nautilus-python/extensions/wezterm-nautilus.py

%files
%license LICENSE.md
%doc README.md docs/
%{_bindir}/open-wezterm-here
%{_bindir}/wezterm
%{_bindir}/wezterm-gui
%{_bindir}/wezterm-mux-server
%{_bindir}/strip-ansi-escapes
/usr/share/zsh/site-functions/_wezterm
/etc/bash_completion.d/wezterm
/usr/share/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
/usr/share/applications/org.wezfurlong.wezterm.desktop
/usr/share/metainfo/org.wezfurlong.wezterm.appdata.xml
/usr/share/nautilus-python/extensions/wezterm-nautilus.py*
/etc/profile.d/*

%changelog
%autochangelog
