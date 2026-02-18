%global debug_package %{nil}

Name:    bun-bin
# renovate: datasource=github-releases depName=oven-sh/bun extractVersion=true
Version: 1.3.9
Release: 1%{?dist}
Summary: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one
License: MIT
URL:     https://github.com/oven-sh/bun
Source0: %{url}/releases/download/bun-v%{version}/bun-linux-x64.zip
Source1: %{url}/releases/download/bun-v%{version}/bun-linux-aarch64.zip
Source2: https://raw.githubusercontent.com/oven-sh/bun/refs/tags/bun-v%{version}/LICENSE.md

ExclusiveArch: x86_64 aarch64
Requires: glibc
Conflicts: bun

%description

%prep
%ifarch x86_64
%setup -c -T -a 0
cp bun-linux-x64/bun ./
%endif

%ifarch aarch64
%setup -c -T -a 1
cp bun-linux-aarch64/bun ./
%endif

cp %{SOURCE2} ./

%install
install -D --mode=755 bun "%{buildroot}%{_bindir}/bun"
ln -s bun %{buildroot}%{_bindir}/bunx

# completions
mkdir -p %{buildroot}%{bash_completions_dir}
./bun completions > %{buildroot}%{bash_completions_dir}/bun.sh

%files
%license LICENSE.md
%{_bindir}/bun
%{_bindir}/bunx
%{bash_completions_dir}/bun.sh

%changelog
%autochangelog
