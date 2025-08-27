%global debug_package %{nil}
%global bgname lakeside

Name:       backgrounds-lakeside
Version:    0.5.0
Release:    1%{?dist}
License:    CC-BY-NC-SA-4.0
Summary:    Lakeside Time of Day backgrounds

URL:        https://github.com/lukasgierth/fedora-packages
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}

BuildArch:      noarch

%description
This package provides the Lakeside Time of Day backgrounds. The dynamic backgrounds updates
according to the time of day. The images are from a project created by Louis Coyle.
Although this package will install the backgrounds in all Desktop Environments, the dynamic
feature is only available in GNOME (and Budgie).

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0755 \
    %{buildroot}%{_datadir}/backgrounds/%{bgname} \
    %{buildroot}%{_datadir}/gnome-background-properties

install -Dpm 0644 images/*.jxl -t %{buildroot}%{_datadir}/backgrounds/%{bgname}
install -Dpm 0644 lakeside-dynamic.xml -t %{buildroot}%{_datadir}/backgrounds/%{bgname}
install -Dpm 0644 lakeside-gnome.xml -t %{buildroot}%{_datadir}/gnome-background-properties

%files
%{_datadir}/backgrounds/%{bgname}/*
%{_datadir}/gnome-background-properties/lakeside-gnome.xml

%changelog
%autochangelog
