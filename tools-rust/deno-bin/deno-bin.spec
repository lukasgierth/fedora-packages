%global debug_package %{nil}

Name:    deno-bin
# renovate: datasource=github-releases depName=denoland/deno extractVersion=true
Version: 2.6.6
Release: 1%{?dist}
Summary: A modern runtime for JavaScript and TypeScript.
License: MIT
URL:     https://github.com/denoland/deno
Source0: %{url}/releases/download/v%{version}/deno-x86_64-unknown-linux-gnu.zip
Source1: %{url}/releases/download/v%{version}/deno-aarch64-unknown-linux-gnu.zip
Source2: https://raw.githubusercontent.com/denoland/deno/refs/tags/v%{version}/LICENSE.md

ExclusiveArch: x86_64 aarch64
Requires: glibc
Conflicts: deno

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
install -D --mode=755 deno "%{buildroot}%{_bindir}/deno"

# completions
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
./deno completions bash > %{buildroot}%{bash_completions_dir}/deno.sh
./deno completions fish > %{buildroot}%{fish_completions_dir}/deno.fish
./deno completions zsh > %{buildroot}%{zsh_completions_dir}/_deno

%files
%license LICENSE.md
%{_bindir}/deno
%{bash_completions_dir}/deno.sh
%{fish_completions_dir}/deno.fish
%{zsh_completions_dir}/_deno

%changelog
%autochangelog
