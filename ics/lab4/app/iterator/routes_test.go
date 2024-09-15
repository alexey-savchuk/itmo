package routes_test

import (
	routes "bus-ticket-sales/iterator"
	"database/sql"
	"testing"

	"github.com/stretchr/testify/require"
	_ "modernc.org/sqlite"
)

func TestSomething(t *testing.T) {
	db, err := sql.Open("sqlite", "file:routes.db")
	require.NoError(t, err)

	repo := routes.NewRepo(db)

	t.Run("try Get", func(t *testing.T) {
		route, err := repo.Get(1)
		require.NoError(t, err)

		t.Logf("got route %v\n", route)
	})

	t.Run("Try GetAll", func(t *testing.T) {
		var (
			allRoutes    []*routes.Route
			iterationErr error
		)

		err := repo.GetAll(func(route *routes.Route, err error) (stop bool) {
			if err != nil {
				iterationErr = err
				return true
			}
			allRoutes = append(allRoutes, route)
			return false
		})
		require.NoError(t, err)
		require.NoError(t, iterationErr)

		for _, route := range allRoutes {
			t.Logf("got route %v\n", route)
		}
	})
}
