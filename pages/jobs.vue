<template>
    <section>
        {{ msg }}
        <form method="POST" action="/">
            <v-text-field
                v-validate="'required|max:10'"
                v-model="name"
                :counter="10"
                :error-messages="errors.collect('name')"
                label="Name"
                data-vv-name="name"
                required
        ></v-text-field>
        </form>
    </section>
</template>


<script>
import axios from 'axios'

export default {
  name: 'Ping',
  data () {
    return {
      msg: '',
      name: ''
    }
  },
  methods: {
    getMessage () {
      const path = 'http://localhost:5000/'
      axios.get(path)
        .then((res) => {
          console.log('response:', res)
          this.msg = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    }
  },
  created () {
    this.getMessage()
  }
}
</script>