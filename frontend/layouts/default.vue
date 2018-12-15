<template>
  <v-app>
    <v-toolbar fixed app :clipped-left="clipped">
        <v-img src="/pacific_bridge_logo.png" max-width="180"/>
        <v-toolbar-items class="hidden-sm-and-down">
            <v-btn flat to="/">Home</v-btn>
            <v-btn flat to="/opportunities">Opportunities</v-btn>
            <v-btn flat to="/jobs">Jobs</v-btn>
        </v-toolbar-items>
        <v-spacer></v-spacer>
        <v-btn
            icon
            @click.stop="rightDrawer = !rightDrawer"
        >
            <v-icon>menu</v-icon>
        </v-btn>
    </v-toolbar>

    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>

    <v-navigation-drawer
      temporary
      :right="right"
      v-model="rightDrawer"
      fixed
    >
      <v-list>
        <v-list>
            <v-list-tile
            router
            :to="item.to"
            :key="i"
            v-for="(item, i) in items"
            exact
            >
            <v-list-tile-action>
                <v-icon v-html="item.icon"></v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
                <v-list-tile-title v-text="item.title"></v-list-tile-title>
            </v-list-tile-content>
            </v-list-tile>
        </v-list>
      </v-list>
    </v-navigation-drawer>
    <v-footer :fixed="fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        clipped: false,
        drawer: true,
        fixed: false,
        items: [
          { icon: 'apps', title: 'Home', to: '/' },
          { icon: 'bubble_chart', title: 'Opportunities', to: '/opportunities' },
          { icon: 'school', title: 'Jobs', to: '/jobs' }
        ],
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'Pacific Bridge'
      }
    }
  }
</script>
