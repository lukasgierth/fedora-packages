%global debug_package %{nil}

Name:       pangolin-cli
# renovate: datasource=github-releases depName=fosrl/cli extractVersion=true
Version:    0.6.0
Release:    1%{?dist}
Summary:    Pangolin CLI tool and VPN client
License:    AGPL-3.0 AND Fossorial-Commercial-License
URL:        https://github.com/fosrl/cli
Source:     %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang

%description

%prep
%autosetup -n cli-%{version}

%build
export GOTOOLCHAIN=auto
go build \
    -ldflags "-s -w" \
    -o _build/%{name}
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}/
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
