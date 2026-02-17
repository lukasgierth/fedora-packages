%global debug_package %{nil}

Name:       doggo
# renovate: datasource=github-releases depName=mr-karan/doggo extractVersion=true
Version:    1.1.4
Release:    1%{?dist}
Summary:    Command-line DNS Client for Humans. Written in Golang
License:    GPL-3.0-or-later
URL:        https://github.com/mr-karan/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.25.5

%description

%prep
%autosetup -n %{name}-%{version}

%build
go build \
    -ldflags "-X main.buildVersion=%{version} -s -w" \
    -o _build/%{name} \
    ./cmd/doggo
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
_build/%{name} completions bash > %{buildroot}%{bash_completions_dir}/%{name}
_build/%{name} completions fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
_build/%{name} completions zsh > %{buildroot}%{zsh_completions_dir}/_%{name}

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
