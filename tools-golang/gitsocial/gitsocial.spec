%global debug_package %{nil}

Name:       gitsocial
# renovate: datasource=github-releases depName=gitsocial-org/gitsocial extractVersion=true
Version:    0.10.1
Release:    1%{?dist}
Summary:    Git-native cross-forge collaboration: posts, issues, PRs, releases, all in your repo
License:    MIT
URL:        https://github.com/gitsocial-org/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang

Requires: git

%description

%prep
%autosetup -n gitsocial-%{version}

%build
export GOTOOLCHAIN=auto
go build \
	-C library \
    -ldflags "-X main.version=%{version} -s -w" \
    -o ../_build/%{name} \
	./cli
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
_build/%{name} completion bash > %{buildroot}%{bash_completions_dir}/%{name}
_build/%{name} completion fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
_build/%{name} completion zsh > %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
