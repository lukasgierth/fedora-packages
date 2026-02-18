%global debug_package %{nil}
%global __strip /bin/true

Name:    opencode-bin
# renovate: datasource=github-releases depName=anomalyca/opencode extractVersion=true
Version: 1.2.6
Release: 1%{?dist}
Summary: The open source coding agent.
License: MIT
URL:     https://github.com/anomalyco/opencode
Source0: %{url}/releases/download/v%{version}/opencode-linux-x64.tar.gz
Source1: %{url}/releases/download/v%{version}/opencode-linux-arm64.tar.gz
Source2: https://raw.githubusercontent.com/anomalyco/opencode/refs/tags/v%{version}/LICENSE

ExclusiveArch: x86_64 aarch64

Requires: glibc
Requires: fzf
Requires: ripgrep

Conflicts: opencode

%description

%prep
%ifarch x86_64
%setup -c -T -a 0
%endif

%ifarch aarch64
%setup -c -T -a 1
%endif

cp %{SOURCE2} ./

%install
install -D --mode=755 opencode "%{buildroot}%{_bindir}/opencode"

# completions
mkdir -p %{buildroot}%{bash_completions_dir}
./opencode completion > %{buildroot}%{bash_completions_dir}/opencode.sh

%files
%license LICENSE
%{_bindir}/opencode
%{bash_completions_dir}/opencode.sh

%changelog
%autochangelog
