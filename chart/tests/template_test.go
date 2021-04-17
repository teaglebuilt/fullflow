package tests

import (
	"testing"

	apps "k8s.io/api/apps/v1"

	"github.com/gruntwork-io/terratest/modules/helm"
)

func TestPodTemplateRendersContainerImage(t *testing.T) {
	helmChartPath := "../../chart"
	options := &helm.Options{
		SetValues: map[string]string{"image": "teaglebuilt/fullflow:dev"},
	}
	output := helm.RenderTemplate(t, options, helmChartPath, "pod", []string{"templates/lab/deployment.yaml"})

	var deployment apps.Deployment
	helm.UnmarshalK8SYaml(t, output, &deployment)

	expectedContainerImage := "teaglebuilt/fullflow:dev"
	notebookContainer := deployment.Spec.Template.Spec.Containers[0].Image

	if notebookContainer != expectedContainerImage {
		t.Fatal("Container image does not match expected")
	}
}
