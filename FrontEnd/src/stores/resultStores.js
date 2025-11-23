import { reactive } from "vue";

export const resultStore = reactive({
  analysis: "",
  recommendations: [],
  confidence: 0,
});
