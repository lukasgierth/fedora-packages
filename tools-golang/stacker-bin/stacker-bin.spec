%global debug_package %{nil}

Name:    stacker-bin
# renovate: datasource=github-releases depName=project-stacker/stacker extractVersion=true
Version: 1.1.5
Release: 1%{?dist}
Summary: A vendor-neutral OCI-native container image (tgz, squashfs, erofs) builder (purely based on OCI Image Specification)
License: Apache-2.0
URL:     https://github.com/project-stacker/stacker
Source0: %{url}/releases/download/v%{version}/stacker-linux-amd64
Source1: %{url}/releases/download/v%{version}/stacker-linux-arm64
Source2: https://raw.githubusercontent.com/project-stacker/stacker/refs/tags/v%{version}/LICENSE

ExclusiveArch: x86_64 aarch64
Requires: glibc
Conflicts: stacker

%description

%prep
%ifarch x86_64
cp %{SOURCE0} stacker
%endif

%ifarch aarch64
cp %{SOURCE1} stacker
%endif

cp %{SOURCE2} ./

%install
install -D --mode=755 stacker "%{buildroot}%{_bindir}/stacker"

%files
%license LICENSE
%{_bindir}/stacker

%changelog
%autochangelog
