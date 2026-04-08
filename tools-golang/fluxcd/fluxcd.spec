%global debug_package %{nil}

Name:       fluxcd
# renovate: datasource=github-releases depName=fluxcd/flux2 extractVersion=true
Version:    2.8.3
Release:    2%{?dist}
Summary:    Open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit.
License:    Apache-2.0
URL:        https://github.com/fluxcd/flux2
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang
BuildRequires: kustomize

%description

%prep
%autosetup -n flux2-%{version}

%build
export GOTOOLCHAIN=auto
export BUILD_DATE=$(date --iso-8601)
make cmd/flux/.manifests.done
go build \
    -ldflags "-X main.VERSION=%{VERSION} -s -w" \
    -o _build/%{name} \
	./cmd/flux
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} %{buildroot}%{_bindir}/flux
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
_build/%{name} completion bash > %{buildroot}%{bash_completions_dir}/flux
_build/%{name} completion fish > %{buildroot}%{fish_completions_dir}/flux.fish
_build/%{name} completion zsh > %{buildroot}%{zsh_completions_dir}/_flux

%files
%license LICENSE
%doc README.md
%{_bindir}/flux
%{_mandir}/man1/*.1*
%{bash_completions_dir}/flux
%{fish_completions_dir}/flux.fish
%{zsh_completions_dir}/_flux

%changelog
%autochangelog
