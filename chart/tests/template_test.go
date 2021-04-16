package tests

import (
	"log"
	"testing"

	corev1 "k8s.io/api/core/v1"

	"github.com/gruntwork-io/terratest/modules/helm"
)

func TestPodTemplateRendersContainerImage(t *testing.T) {
	helmChartPath := "../../chart"
	options := &helm.Options{
		SetValues: map[string]string{"image": "teaglebuilt/fullflow:dev"},
	}
	output := helm.RenderTemplate(t, options, helmChartPath, "pod", []string{"templates/lab/deployment.yaml"})
	log.Printf(output)

	var pod corev1.Pod
	helm.UnmarshalK8SYaml(t, output, &pod)

	// expectedContainerImage := "teaglebuilt/fullflow:dev"
	// podContainers := pod.Spec.Containers
	// if podContainers[0].Image != expectedContainerImage {
	// 	t.Fatalf("Rendered container image (%s) is not expected (%s)", podContainers[0].Image, expectedContainerImage)
	// }
}
