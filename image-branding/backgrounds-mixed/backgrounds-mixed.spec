%global debug_package %{nil}
%global bgname mixed

Name:       backgrounds-mixed
Version:    2026.04.1
Release:    1%{?dist}
License:    CC-BY-NC-SA-4.0
Summary:    mixed backgrounds
URL:        https://github.com/lukasgierth/fedora-packages
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}

BuildArch:      noarch

%description
https://www.gnome-look.org/p/2035792
https://www.gnome-look.org/p/2036892
https://www.gnome-look.org/p/2351770
https://www.gnome-look.org/p/2336034
https://www.gnome-look.org/p/2326951
https://www.gnome-look.org/p/2328697

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0755 \
    %{buildroot}%{_datadir}/backgrounds/%{bgname} \
    %{buildroot}%{_datadir}/gnome-background-properties

cp -r images/* -t %{buildroot}%{_datadir}/backgrounds/%{bgname}
install -Dpm 0644 mixed-gnome.xml -t %{buildroot}%{_datadir}/gnome-background-properties

%files
%{_datadir}/backgrounds/%{bgname}/*
%{_datadir}/gnome-background-properties/mixed-gnome.xml

%changelog
%autochangelog
