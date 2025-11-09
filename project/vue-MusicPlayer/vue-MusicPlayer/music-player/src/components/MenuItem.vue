<script setup>
import { ref, toRefs, watchEffect } from "vue";
import { useRoute } from "vue-router";
import {
  HomeIcon,
  MagnifyingGlassIcon,
  BookOpenIcon,
  PlusCircleIcon,
  HeartIcon,
} from "@heroicons/vue/24/outline";
const route = useRoute();

const props = defineProps({
  iconString: String,
  pageUrl: String,
  name: String,
});

const icons = {
  home: HomeIcon,
  search: MagnifyingGlassIcon,
  library: BookOpenIcon,
  playlist: PlusCircleIcon,
  liked: HeartIcon,
};

const { iconString, pageUrl, name } = toRefs(props);
let textIsHover = ref(false);

watchEffect(() => {
  textIsHover.value = route.path == pageUrl.value;
});

const isHover = () => {
  if (route.path == pageUrl.value) return;
  textIsHover.value = !textIsHover.value;
};
</script>

<template>
  <li
    class="flex items-center justify-start pb-4 cursor-pointer"
    @mouseenter="isHover()"
    @mouseleave="isHover()"
  >
    <component
      :is="icons[iconString]"
      :class="[textIsHover ? 'text-white' : 'text-gray-400', 'h-6 w-6']"
      aria-hidden="true"
    />
    <div
      :class="textIsHover ? 'text-white' : 'text-gray-400'"
      class="font-semibold text-[14px] ml-4 mt-0.5"
    >
      <span :class="route.path == pageUrl ? 'text-white' : ''">{{ name }}</span>
    </div>
  </li>
</template>
