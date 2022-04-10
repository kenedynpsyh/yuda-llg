<template>
  <div>
    <div class="py-4 px-12">
      <vs-button class="font-semibold" @click="AddServer()"
        >Tambah Server</vs-button
      >
      <div class="px-2">
        <div class="font-bold">Pilih Server :</div>
        <div class="flex flex-wrap">
          <div v-for="(items, index) in data" :key="index" class="pr-12">
            <div class="flex items-center">
              <span class="font-bold mr-2 text-sm">#{{ index + 1 }}</span>
              <vs-radio
                v-for="item in items.choose"
                :key="item"
                success
                class="capitalize font-semibold text-sm"
                v-model="options"
                :val="`${item} ${index}`"
                >{{ item }}</vs-radio
              >
            </div>
            <pre class="text-sm pt-4">{{ items.results }}</pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import axios, { AxiosResponse } from "axios";

@Component({
  name: "Default",
})
export default class Index extends Vue {
  data = [
    {
      choose: ["indodax", "gateio", "huobi"],
      results: "",
      index: 0,
      options: "",
    },
  ];
  options = "";
  numbers = 1;

  $vs: any;

  @Watch("options")
  onOptionsChanges(newVal, oldVal) {
    axios
      .post("http://localhost:5000", { data: newVal.split(" ")[0] }, {})
      .then((res: AxiosResponse<any>) => {
        this.data = this.data.map((item, index) =>
          index === parseInt(newVal.split(" ")[1])
            ? {
                ...item,
                index: parseInt(newVal.split(" ")[1]),
                options: newVal.split(" ")[0],
                results: res.data.message,
              }
            : item
        );
      });
    return newVal;
  }

  AddServer() {
    this.data.push({
      choose: ["indodax", "gateio", "huobi"],
      results: "",
      index: 0,
      options: "",
    });
  }

  onUpdate() {
    this.numbers += 1;
    if (10 <= this.numbers) {
      this.data.map((item) => {
        if (item.results) {
          axios
            .post("http://localhost:5000", { data: item.options }, {})
            .then((res: AxiosResponse<any>) => {
              this.data = this.data.map((item, index) =>
                index === item.index
                  ? { ...item, results: res.data.message }
                  : item
              );
            });
          this.$vs.notification({
            title: "Successfulyy",
            color: "success",
            position: "top-right",
            text: `Data telah diperbarui`,
          });
        }
      });
      this.numbers = 0;
    }

    this.$forceUpdate();
  }

  mounted() {
    this.$forceUpdate();
  }

  updated() {
    const inter = setInterval(() => {
      this.onUpdate();
    }, 20000);
  }
}
</script>
