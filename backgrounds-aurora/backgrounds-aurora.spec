%global debug_package %{nil}
%global bgname aurora

Name:       backgrounds-aurora
Version:    0.3.0
Release:    1%{?dist}
License:    CC-BY-NC-SA-4.0
Summary:    Aurora Time of Day backgrounds
URL:        https://github.com/lukasgierth/fedora-packages
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}

BuildArch:      noarch

%description
This package provides the Aurora Time of Day backgrounds. The dynamic backgrounds updates
according to the time of day. I could not find the original owner of the images.
Although this package will install the backgrounds in all Desktop Environments, the dynamic
feature is only available in GNOME (and Budgie).

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0755 \
    %{buildroot}%{_datadir}/backgrounds/%{bgname} \
    %{buildroot}%{_datadir}/gnome-background-properties

install -Dpm 0644 images/*.jxl -t %{buildroot}%{_datadir}/backgrounds/%{bgname}
install -Dpm 0644 aurora-dynamic.xml -t %{buildroot}%{_datadir}/backgrounds/%{bgname}
install -Dpm 0644 aurora-gnome.xml -t %{buildroot}%{_datadir}/gnome-background-properties

%files
%{_datadir}/backgrounds/%{bgname}/*
%{_datadir}/gnome-background-properties/aurora-gnome.xml

%changelog
%autochangelog
